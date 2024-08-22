## Propósito
Estudio de los regex avanzado y automatización de apuntes de tryhackme

# Documentación 
Necesitarás las librerías

```sh
pip install beautifulsoup4 lxml
```

## ¿Que hace el programa? 

*Primero necesitaremos entender que . en regex de python no considera saltos de línea por lo tanto pondremos el parámetro DOTALL para que el punto también sean saltos de línea. 

```python
import re
pattern = re.compile(r'.*', re.DOTALL)
```

Elimina las etiquetas `<script>` del html y todo lo que hay dentro 

```python
<script[ ]?[>]?.*</script>
```

```vim
<script\_s\{0,1}\_.\{-}<\/script>
```

Eliminar ```<headers>```

```python
<header .*</header>
```

```vim
<header\_.\{-}<\/header>
```

Eliminar `<style>` 

```vim
<style\_.\{-}<\/style>
```

Eliminar `<svg>`

```python
<svg[ ]?>?.*</svg>
```

```vim
<svg\_s\{0,1}\_.\{-}<\/svg>
```

Eliminar `<lottie-player>`

```python
import re
pattern = re.compile(r'.*', re.DOTALL)
```

```vim
<lottie-player\_.\{-}<\/lottie-player>
```

Eliminar `<button>`

```python
<button .*</button>
```

```vim
<button\_.\{-}<\/button>
```

Eliminar `<div class="sc-dGVqZU gEQPPg">`

```python
<div.*class=\"sc-dGVqZU[ ]gEQPPg\".*>.*</div>
```

Eliminar `<div data-sentry-component="HelperTooltipWrapper">`

Eliminar `<div id="room-banner">`

```vim
:%s/<div id="room-banner"\_.\{-}<\/div>//g
```

Eliminar `<div class="sc-goWbiw jVwxWH">`

```vim
:%s/<div\_.\{-}class="sc-goWbiw jVwxWH">\_.\{-}<\/div>
```

Eliminar div class

```vim
:%s/<div\_.\{-}class="sc-eqUAAy iXyexf">\_.\{-}<\/div>
```

Eliminar `<div class=sc-eqUAAy dKvyXO>`

Eliminar footer
```python
import re
pattern = re.compile(r'.*', re.DOTALL)
```

```vim
<footer\_.\{-}<\/footer>
```
