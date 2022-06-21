# Newsuty Landing
Esta es la landing page de Newsuty, desarollada con angular y sass.<br/>
Para servir la landing page se esta utilizando flask.<br/>
La ruta / contiene la landing page<br/>
<br/>
La ruta /link?url=url devolverá la url parseda usando The Open Graph protocol<br/>
ejemplo /link?url=https://www.malagahoy.es/malaga/detenidos-Malaga-vuelo-Londres-documentacion-falsa_0_1694531960.html<br/>

{"title":"Dos detenidos en M\u00e1laga por tratar de embarcar en un vuelo a Londres con documentaci\u00f3n falsa","url":"https://www.malagahoy.es/malaga/detenidos-Malaga-vuelo-Londres-documentacion-falsa_0_1694531960.html","url_image":"https://www.malagahoy.es/2022/02/05/malaga/policia-nacional-aeropuerto-Malaga_1654044771_151477900_1200x675.jpg"}
<br/>
# Dependecias python
pip install python-opengraph flask
# Dependecias Angular
npm install
