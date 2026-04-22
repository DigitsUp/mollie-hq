from PIL import Image, ImageDraw, ImageFont
import textwrap, os

def generate_card(label, headline, body, output_path):
    """
    MBM tweet card generator.
    label: e.g. "THE FAIL" / "THE WIN" / "THE WEIRD ONE" / "THE USE CASE"
    headline: 2-line string with \n
    body: plain string, will be auto-wrapped
    output_path: where to save the PNG
    """
    W, H = 1080, 1080
    PINK = '#FF3CAC'
    PAD = 70

    font_bold = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 78)
    font_med = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 38)
    font_label = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 44)
    font_brand = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 34)

    wrapped_body = textwrap.fill(body, width=48)
    brand = "My Bad, Mollie."

    dummy = Image.new('RGB', (W, H))
    d = ImageDraw.Draw(dummy)
    lh = d.textbbox((0,0), label, font=font_label)[3]
    hh = d.textbbox((0,0), headline, font=font_bold)[3]
    bh = d.textbbox((0,0), wrapped_body, font=font_med)[3]
    brh = d.textbbox((0,0), brand, font=font_brand)[3]

    divider_h = 4
    brand_gap = 20
    bottom_margin = 80
    total_content = lh + hh + bh + divider_h + brand_gap + brh + bottom_margin
    top_bar = 8
    available = H - top_bar - total_content
    gap = available // 4
    margin_top = top_bar + gap

    img = Image.new('RGB', (W, H), color='#0a0a0a')
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, top_bar], fill=PINK)

    y = margin_top
    draw.text((PAD, y), label, font=font_label, fill=PINK)
    y += lh + gap
    draw.text((PAD, y), headline, font=font_bold, fill='#ffffff')
    y += hh + gap
    draw.text((PAD, y), wrapped_body, font=font_med, fill='#cccccc')
    y += bh + gap
    draw.rectangle([PAD, y, PAD+280, y+divider_h], fill=PINK)
    y += divider_h + brand_gap
    draw.text((PAD, y), brand, font=font_brand, fill='#ffffff')

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    return output_path

if __name__ == "__main__":
    generate_card(
        label="THE FAIL",
        headline="He checked every box.\nJust not that one.",
        body="Marcus's AI helped run the perfect April Fools campaign. Legal approved it. Highest click rate ever. But the company was in active litigation. He was out by noon.",
        output_path="/Users/minigrill/.openclaw/workspace/projects/mybadmollie/tweet-marcus-final.png"
    )
    print("Done")
