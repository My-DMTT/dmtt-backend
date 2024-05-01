from docxtpl import DocxTemplate

doc = DocxTemplate("temp.docx")
data = {
    "company_name": "Abdusalom Yuksak Kelajak",
    "dmtt_name": "1-dmtt",
    "dmtt_address": "Toshloq",
    "company_phone": "+998905360968",
    "items": [["Olma", 5], ["Olma", 5], ["Olma", 5], ["Olma", 5], ["Olma", 5]]
}

doc.render(context=data)

doc.save("fs.docx")
