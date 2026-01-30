import os
import re

# Note: commented out code-snippets are for grid generation. 

# IMG_DIRs = ["Logos"]
IMG_DIRs = ["Front-wing","Rear-wing","InterIIT","FEM"]
HTML_FILE = "gallery.html"
# HTML_FILE = "index.html"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html = f.read()

# Capture indentation before the marker
match = re.search(r"(\n[ \t]*)<!-- GALLERY START -->", html)
indent = match.group(1)[1:] if match else ""

gallery_lines = []

for IMG_DIR in IMG_DIRs:
    for root, _, files in os.walk(IMG_DIR):
        images = [f for f in files if f.lower().endswith(('.png','.jpg','.jpeg','.webp','.PNG'))]
        if images:
            section = os.path.basename(root)
            gallery_lines.append(f'{indent}<section id="{section}" class="body-page backgnd">')
            # gallery_lines.append(f'{indent}<div class="body-page">')
            gallery_lines.append(f"{indent}    <h3>{section}</h3>")
            gallery_lines.append(f"{indent}    <div class='gallery'>")
            # gallery_lines.append(f"{indent}    <div class='grid'>")
            for img in images:
                path = f"{root}/{img}".replace("\\", "/")
                gallery_lines.append(f"{indent}        <div class='img-card'><img src='{path}' loading='lazy'></div>")
            gallery_lines.append(f"{indent}    </div>")
            gallery_lines.append(f"{indent}</section>")
            # gallery_lines.append(f"{indent}</div>")
            gallery_lines.append("")

gallery_html = "\n".join(gallery_lines)

new_html = re.sub(
    r"<!-- GALLERY START -->.*?<!-- GALLERY END -->",
    f"<!-- GALLERY START -->\n{gallery_html}\n{indent}<!-- GALLERY END -->",
    html,
    flags=re.S
)

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(new_html)

print("\n\nGallery updated (existing HTML preserved).\n\n")