from PIL import Image
import sys

def to_bits(data: bytes) -> str:
    return ''.join(f'{b:08b}' for b in data)

def from_bits(bits: str) -> bytes:
    return bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))

def embed(image_path, message, output_path):
    img = Image.open(image_path).convert('RGB')
    pixels = img.load()
    payload = message.encode('utf-8')
    header = len(payload).to_bytes(4, 'big')  # 4 bytes con longitud
    full = header + payload
    bits = to_bits(full)

    w, h = img.size
    capacity = w * h * 3
    if len(bits) > capacity:
        raise ValueError(f"Mensaje muy grande: {len(bits)} bits > {capacity}")

    idx = 0
    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y]
            if idx < len(bits):
                r = (r & ~1) | int(bits[idx]); idx += 1
            if idx < len(bits):
                g = (g & ~1) | int(bits[idx]); idx += 1
            if idx < len(bits):
                b = (b & ~1) | int(bits[idx]); idx += 1
            pixels[x, y] = (r, g, b)
            if idx >= len(bits):
                img.save(output_path, 'PNG')
                return

def extract(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = img.load()
    w, h = img.size
    bits = []
    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y]
            bits.extend([str(r & 1), str(g & 1), str(b & 1)])

    length = int(''.join(bits[:32]), 2)
    if length <= 0 or length > (len(bits) - 32) // 8:
        raise ValueError("No se detectó mensaje o cabecera corrupta")
    msg_bits = bits[32:32 + length * 8]
    return from_bits(''.join(msg_bits)).decode('utf-8', errors='replace')

if __name__ == '__main__':
    if sys.argv[1] == 'embed':
        embed(sys.argv[2], sys.argv[3], sys.argv[4])
        print(f"Guardado en {sys.argv[4]}")
    elif sys.argv[1] == 'extract':
        print(extract(sys.argv[2]))
        