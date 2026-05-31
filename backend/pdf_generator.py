from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet

import re


def clean_text(text):

    if not text:
        return ""

    text = re.sub(r"#+", "", text)
    text = re.sub(r"\*\*", "", text)
    text = re.sub(r"\*", "", text)

    return text


def add_section(content, title, text, styles):

    content.append(
        Paragraph(title, styles["Heading1"])
    )

    content.append(
        Spacer(1, 10)
    )

    text = clean_text(text)

    for line in text.split("\n"):

        if line.strip():

            content.append(
                Paragraph(
                    line.strip(),
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(1, 4)
            )

    content.append(
        Spacer(1, 15)
    )


def generate_pdf(
    change,
    impact,
    risk,
    training,
    risk_score
):

    pdf_file = "enterprise_change_report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Enterprise Change Impact Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"<b>Change Request:</b> {change}",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    add_section(
        content,
        "Impact Analysis",
        impact,
        styles
    )

    add_section(
        content,
        "Risk Analysis",
        risk,
        styles
    )

    add_section(
        content,
        "Training Plan",
        training,
        styles
    )

    content.append(
        Paragraph(
            f"<b>Risk Score:</b> {risk_score}/100",
            styles["Heading2"]
        )
    )

    doc.build(content)

    return pdf_file