from openai import OpenAI

client = OpenAI(api_key='sk-...')

with open('article.txt', 'r', encoding='utf-8') as file:
    article = file.read()

prompt = f"""
na podstawie tego artykułu, podaj mi kod do stworzenia strony internetowej na podstawie tych wytycznych:

Wytyczne:
Kod artykułu wygenerowany przez AI powinien spełniać następujące wytyczne:
• Najważniejsze! Nie dodawaj żadnych znaczników ani komentarzy takich jak np. ```html ```
• Użycie odpowiednich tagów HTML do strukturyzacji treści.
• Dodaj odpowiednio znaczniki <div> oraz atrybuty class. Zrób to hybrydowo tzn. każdy <div> powinien mieć klase generyczną typu section, container, oraz klase spersonalizowaną pod względem treści w maks dwóch słowach.
• Brak kodu CSS ani JavaScript. Zwrócony kod powinien zawierać wyłącznie zawartość do
wstawienia pomiędzy tagami <body> i </body>. Nie dołączaj znaczników <html>,
<head> ani <body>.
• Zwrócony kod nie może mieć znaczników <body>.

Artykuł:
{article}
"""

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a senior frontend developer."},
        {
            "role": "user",
            "content": prompt
        }
    ]
)

content = completion.choices[0].message.content

prompt = f"""
Zmodyfikuj zawartości sekcji <body> w html na podstawie tych wytycznych:

• Dla każdego <div> wstaw minimum jedno miejsce, gdzie warto wstawić grafiki – oznaczamy je z użyciem tagu <img> z atrybutem src="image_placeholder.jpg". 
• Dodaj atrybut alt do każdego obrazka z dokładnym promptem, który możemy użyć do wygenerowania grafiki. Prompt do generowania grafiki musi być według najlepszych standardów. Prompt musi zawierać podmiot, opis oraz styl/estetyke
• Umieść podpisy pod grafikami używając <figcaption>.
• Nie dodawaj zadnych znaczników niż te które określają grafikę
• Nie dodawaj żadnych znaczników ani komentarzy takich jak np. ```html ```

Sekcja <body>:
{content}
"""

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a senior frontend developer."},
        {
            "role": "user",
            "content": prompt
        }
    ]
)

content = completion.choices[0].message.content

with open('artykul.html', 'w', encoding='utf-8') as file:
    file.write(content)