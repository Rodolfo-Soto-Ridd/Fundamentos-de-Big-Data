# Sección 1: Preguntas abiertas (5 puntos) 
# 1. ¿Qué son las 5V’s de Big Data? Explica cada una con tus propias palabras y da un ejemplo real para cada una. 

# Las 5V's de Big Data son un modelo que describe las características clave de los conjuntos de datos masivos. 
# Son cinco dimensiones: volumen, velocidad, variedad, veracidad y valor.
# Volumen: Se refiere a la enorme cantidad de datos generados y almacenados. Piensa en la escala de terabytes, 
# petabytes o incluso exabytes. Por ejemplo, los datos de transacciones de una plataforma como Amazon en un solo 
# día son un ejemplo perfecto de volumen masivo.
# Velocidad: Es la rapidez con la que los datos se generan, recopilan y procesan. Los datos en tiempo real son un 
# claro ejemplo de esto. Un sistema de monitoreo de redes sociales, que procesa miles de tweets por minuto, 
# ilustra la velocidad de Big Data.
# Variedad: Se trata de la diversidad de tipos de datos, que pueden ser estructurados (como tablas de Excel), 
# semi-estructurados (como archivos XML o JSON) o no estructurados (como imágenes, videos, correos electrónicos y 
# textos). Los datos recopilados por un hospital que incluyen historiales médicos (estructurados), resultados de 
# radiografías (imágenes no estructuradas) y notas de médicos (texto no estructurado) son un ejemplo de variedad.
# Veracidad: Se relaciona con la calidad, confiabilidad y precisión de los datos. Datos con baja veracidad pueden 
# llevar a análisis erróneos. Por ejemplo, en un sistema de análisis de sentimientos, la veracidad se pone a prueba 
# al distinguir entre opiniones genuinas y comentarios generados por bots, o al interpretar el sarcasmo. 
# Valor: El valor de Big Data radica en la capacidad de extraer información útil y perspicaz que beneficie a la 
# empresa o al usuario. Sin un propósito claro, los datos masivos son solo un montón de bits. El análisis de los 
# datos de tráfico de una ciudad para optimizar las rutas de transporte público y reducir la congestión es un claro 
# ejemplo de cómo los datos se convierten en valor.


# 2. Explica la diferencia entre sistemas locales y sistemas distribuidos en el contexto de Big Data. 

# En el contexto de Big Data, la principal diferencia entre un sistema local y un sistema distribuido radica en cómo 
# se gestiona el almacenamiento y el procesamiento de los datos.
# Sistemas locales: En este tipo de arquitectura, tanto el almacenamiento como el procesamiento de los datos se 
# realizan en un solo equipo o servidor. Es una solución viable para conjuntos de datos más pequeños o cuando la 
# velocidad de procesamiento no es la máxima prioridad. La limitación principal es la escalabilidad y la tolerancia a 
# fallos. Si el servidor falla, todo el sistema se cae.
# Sistemas distribuidos: Estos sistemas dividen los datos y las tareas de procesamiento entre múltiples máquinas 
# interconectadas en una red. Cada máquina, o "nodo", se encarga de una parte del trabajo. Las principales ventajas 
# son la escalabilidad (se pueden añadir más nodos para manejar más datos), la tolerancia a fallos (si un nodo falla, 
# el sistema sigue funcionando) y la eficiencia (el procesamiento se realiza en paralelo). Un ejemplo clásico es el 
# ecosistema de Hadoop, que distribuye los datos en un sistema de archivos (HDFS) y el procesamiento entre los nodos 
# del clúster.

# 3. Imagina que una empresa necesita procesar grandes volúmenes de datos en tiempo real. 

# Para una empresa que necesita procesar grandes volúmenes de datos en tiempo real, recomendaría una combinación de 
# tecnologías que soporten la ingesta y el procesamiento de flujos de datos continuos.
# Apache Kafka: Es una plataforma de streaming de datos que funciona como un "cerebro" para mover datos de un lugar a 
# otro en tiempo real. Actúa como un sistema de mensajería altamente escalable y tolerante a fallos, permitiendo que 
# múltiples aplicaciones publiquen y se suscriban a flujos de datos. Esto es fundamental para la ingesta de datos en 
# tiempo real.
# Apache Spark Streaming: Es una extensión de Spark que permite procesar flujos de datos. A diferencia de Hadoop, que 
# procesa datos en lotes, Spark Streaming es ideal para analizar datos a medida que llegan. Su capacidad de realizar 
# procesamiento en memoria lo hace extremadamente rápido, lo cual es crucial para análisis en tiempo real.
# Apache Flink: Similar a Spark Streaming, Flink es otro motor de procesamiento de flujos en tiempo real. Se destaca 
# por su capacidad para procesar eventos con una latencia muy baja, lo que lo hace ideal para aplicaciones que requieren 
# una respuesta casi instantánea.
# ¿Por qué estas tecnologías? La combinación de Kafka y Spark o Flink crea un pipeline de datos robusto y escalable. 
# Kafka se encarga de la ingestión y el almacenamiento temporal de los flujos de datos. Posteriormente, Spark Streaming 
# o Flink toman esos flujos y los procesan en memoria casi en tiempo real, permitiendo la detección de patrones 
# o la toma de decisiones inmediata, lo que es imposible con bases de datos relacionales tradicionales.

# ¿Qué tecnologías de Big Data recomendarías y por qué? 
# La combinación de Kafka y Spark o Flink crea un pipeline de datos robusto y escalable. Kafka se encarga de la ingestión 
# y el almacenamiento temporal de los flujos de datos. Posteriormente, Spark Streaming o Flink toman esos flujos y los 
# procesan en memoria casi en tiempo real, permitiendo la detección de patrones o la toma de decisiones inmediata, lo 
# que es imposible con bases de datos relacionales tradicionales.

# Sección 2: Análisis de casos (5 puntos) 
# Caso 1: Elección de almacenamiento y procesamiento Una empresa de telecomunicaciones almacena registros de llamadas, 
# consumo de datos móviles y ubicación de usuarios. Actualmente, estos datos se guardan en bases de datos relacionales, 
# pero el volumen de información ha crecido y se ha vuelto difícil de manejar. 
# ✔ Pregunta: 
# ¿Qué tipo de almacenamiento y procesamiento recomendarías implementar? Explica tu elección y justifica qué ventajas 
# ofrece sobre la solución actual. 

# Recomendación: Para una empresa de telecomunicaciones que maneja registros de llamadas y consumo de datos, recomendaría
#  implementar una solución de almacenamiento en un sistema de archivos distribuido como Hadoop Distributed File System 
# (HDFS) y utilizar un motor de procesamiento como Apache Spark.
# Justificación:
# Almacenamiento (HDFS): Ventajas sobre las bases de datos relacionales: Las bases de datos relacionales tradicionales no 
# están optimizadas para el almacenamiento de datos masivos y no estructurados o semi-estructurados. HDFS, en cambio, está 
# diseñado para manejar petabytes de datos, distribuyéndolos entre múltiples nodos. Esto lo hace altamente escalable y 
# resistente a fallos.
# Optimización para el uso de datos masivos: HDFS permite almacenar datos de diferentes formatos (registros de llamadas, 
# datos de consumo, ubicación) de manera eficiente y a bajo costo, a diferencia de las bases de datos relacionales que 
# requieren un esquema rígido.
# Procesamiento (Apache Spark):
# Ventajas sobre las bases de datos relacionales: A diferencia de las bases de datos relacionales que procesan datos en el 
# lugar de almacenamiento, Spark puede leer los datos de HDFS y procesarlos en memoria. Esta capacidad de computación en 
# memoria es crucial para el análisis de grandes volúmenes de datos de telecomunicaciones, lo que acelera significativamente 
# las consultas y los análisis complejos, como la detección de patrones de uso o la segmentación de clientes. 
# En resumen, esta arquitectura de Big Data es mucho más escalable, económica y flexible para manejar el crecimiento constante 
# de los datos de telecomunicaciones, superando las limitaciones de las bases de datos relacionales en términos de volumen, 
# variedad y velocidad de procesamiento.

# Caso 2: Elección de framework para Big Data Un banco necesita analizar patrones de fraude en transacciones bancarias en 
# tiempo real para prevenir pérdidas económicas. 
# ✔ Pregunta: Entre Hadoop y Spark, ¿cuál recomendarías para este problema? Justifica tu respuesta considerando las 
# características de cada tecnología. 

# Recomendación: Para el análisis de patrones de fraude en transacciones bancarias en tiempo real, recomendaría Apache Spark.
# Justificación:
# Procesamiento en tiempo real: El problema de la detección de fraude bancario requiere una respuesta casi instantánea. 
# Spark se destaca por su capacidad de procesamiento en memoria a través de Spark Streaming, lo que le permite analizar los 
# datos de transacciones a medida que se producen, en milisegundos.
# Versatilidad: Spark incluye bibliotecas integradas como MLlib para aprendizaje automático, que son cruciales para construir 
# y ejecutar modelos que detectan patrones de fraude.
# Diferencias con Hadoop: Hadoop, con su motor de procesamiento MapReduce, está diseñado para el procesamiento por lotes de 
# grandes volúmenes de datos. Aunque es excelente para analizar datos históricos (como la identificación de patrones de fraude 
# a largo plazo), no es adecuado para la detección de fraude en tiempo real debido a su alta latencia y la necesidad de escribir 
# datos en disco entre las etapas de procesamiento. Spark, por el contrario, mantiene los datos en memoria, lo que es fundamental 
# para una respuesta rápida. Por lo tanto, mientras que Hadoop es una base sólida para el almacenamiento de datos, Spark es la 
# herramienta de procesamiento ideal para este caso de uso específico.