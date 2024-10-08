import re # regex
import argparse # Para manejar argumentos

def clean_html(html_content):
    # Eliminar las etiquetas <script> y su contenido
    html_content = re.sub(r'<script.*?</script>', '', html_content, flags=re.DOTALL)
    # Eliminar las etiquetas <header> y su contenido
    html_content = re.sub(r'<header.*?</header>', '', html_content, flags=re.DOTALL)
    # Eliminar las etiquetas <style> y su contenido
    html_content = re.sub(r'<style.*?</style>', '', html_content, flags=re.DOTALL)
    # Reemplazar las etiquetas <svg> por separadores
    html_content = re.sub(r'<svg.*?</svg>', '', html_content, flags=re.DOTALL)
    # Eliminar las etiquetas <lottie-player> y su contenido
    html_content = re.sub(r'<lottie-player.*?</lottie-player>', '', html_content, flags=re.DOTALL)
    # Eliminar todos los <button>
    html_content = re.sub(r'<button.*?</button>', '', html_content, flags=re.DOTALL)
    # Eliminar <div class="sc-dGVqZU gEQPPg"> y su contenido
    html_content = re.sub(r'<div.*?class="sc-dGVqZU[ ]gEQPPg".*?>.*?</div>', '', html_content, flags=re.DOTALL)
    # Eliminar <div data-sentry-component="HelperTooltipWrapper">
    html_content = re.sub(r'<div.*?data-sentry-component="HelperTooltipWrapper".*?>.*?</div>', '', html_content, flags=re.DOTALL)
    # Eliminar <div id="room-banner">
    html_content = re.sub(r'<div id="room-banner".*?</div>', '', html_content, flags=re.DOTALL)
    # Eliminar <div class="sc-goWbiw jVwxWH">
    html_content = re.sub(r'<div.*?class="sc-goWbiw jVwxWH".*?>.*?</div>', '', html_content, flags=re.DOTALL)
    # Eliminar <div class="sc-eqUAAy iXyexf">
    html_content = re.sub(r'<div.*?class="sc-eqUAAy iXyexf".*?>.*?</div>', '', html_content, flags=re.DOTALL)
    # Eliminar <footer> y su contenido
    html_content = re.sub(r'<footer.*?</footer>', '', html_content, flags=re.DOTALL)
    # Eliminar iframes
    html_content = re.sub(r'<iframe.*?></iframe>', '', html_content, flags=re.DOTALL)
    # {Titles of the room}
    html_content = re.sub(r'(Task\ (\d+))(\w*)', r'\3', html_content) # No necesita dotall
   
    return html_content

def process_html_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    cleaned_content = clean_html(html_content)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

def main():
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description='Procesar un archivo HTML.')
    parser.add_argument('input_file', type=str, help='El archivo HTML de entrada')

    # Parsear los argumentos
    args = parser.parse_args()

    # Llamar a la función con los argumentos proporcionados
    print('Resultado generado en result.html')
    process_html_file(args.input_file, 'result.html')

if __name__ == '__main__':
    main()

