# flask-blockchain-app

Librerías necesarias para la creación de una Blockchain con Python:

datetime: El módulo datetime proporciona clases para manipular fechas y horas. Si bien la implementación permite operaciones aritméticas con fechas y horas, su principal objetivo es poder extraer campos de forma eficiente para su posterior manipulación o formateo.

hashlib: Este módulo implementa una interfaz común a diferentes algoritmos de hash y resúmenes de mensajes seguros. Están incluidos los algoritmos de hash FIPS seguros SHA1, SHA224, SHA226, SHA384 y SHA512 (definidos en FIPS 180-2) además del algoritmo MD5 de RSA (definido en Internet RFC 1321). Los términos «hash seguro» y «resumen de mensaje» son intercambiables. Los algoritmos más antiguos fueron denominados resúmenes de mensajes. El término moderno es hash seguro.

json: JSON son las siglas de JavaScript Object Notation. JSON es un formato de datos ligero que se utiliza para el intercambio de datos entre varios lenguajes diferentes. Es fácil de leer para los humanos y fácilmente analizado por las máquinas.

flask: Flask es un micro framework web escrito en Python. Se clasifica como un microframework porque no requiere herramientas o librerías particulares. No tiene capa de abstracción de base de datos, validación de formularios, o cualquier otro componente donde las librerías de terceros preexistentes proporcionan funciones comunes. Sin embargo, Flask admite extensiones que pueden añadir funciones a la aplicación como si estuvieran implementadas en el propio Flask. Existen extensiones para mapeadores objeto-relacionales, validación de formularios, manejo de cargas, varias tecnologías de autenticación abierta y varias herramientas relacionadas con el marco común.

requests: Requests es una biblioteca HTTP para el lenguaje de programación Python. El objetivo del proyecto es hacer que las solicitudes HTTP sean más simples y amigables para los humanos. La versión actual es 2.26.0. Las solicitudes se publican bajo la licencia Apache 2.0.

uuid: Este módulo proporciona objetos UUID inmutables (la clase UUID) y las funciones uuid1(), uuid3(), uuid4(), uuid5() para generar UUIDs de las versiones 1, 3, 4 y 5 como se especifica en el RFC 4122. Si lo único que quieres es un ID único, probablemente debas llamar a uuid1() o a uuid4(). Ten en cuenta que uuid1() puede comprometer la privacidad, ya que crea un UUID que contiene la dirección de red del ordenador. uuid4() crea un UUID aleatorio.

urllib.parse: Este módulo define una interfaz estándar para dividir las cadenas de localizadores uniformes de recursos (URL) en componentes (esquema de direccionamiento, ubicación en la red, ruta, etc.), para volver a combinar los componentes en una cadena de URL, y para convertir una "URL relativa" en una URL absoluta dada una "URL base". El módulo ha sido diseñado para ajustarse a la RFC de Internet sobre Localizadores Uniformes de Recursos Relativos. Admite los siguientes esquemas de URL: file, ftp, gopher, hdl, http, https, imap, mailto, mms, news, nntp, prospero, rsync, rtsp, rtspu, sftp, shttp, sip, sips, snews, svn, svn+ssh, telnet, wais, ws, wss.
