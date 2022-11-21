# p4-encoderOptico

El objetivo de esta práctica es entender el mecanismo que utiliza un encoder usando un sensor óptico. 
Los encoders son los sensores más utilizados para la medición de sistemas rotacionales. El encoder óptico que vamos a utilizar está compuesto por un emisor de luz (normalmente un [fotodiodo](https://como-funciona.co/fotodiodo/))y un receptor ([fototransistor](https://tallerelectronica.com/fototransistor/)). 

El mecanismo es sencillo, cuando el disco gira la señal se hace alternante que es directamente proporcional a la velocidad de rotación del eje, además, se puede calcular la resolución de un encoder con la siguiente imágen:

![fórmula resolución encoder](https://github.com/rsanchez2021/Image/blob/main/Captura%20desde%202022-11-21%2013-29-35.png 'Fórmula encoder')

## Sentido de Giro
Para conocer el sentido de giro del disco, lo más usado es utilizar al mnos dos pares emisor-receptor con un desfase de 1/4 para que la señal se quede desfasada por 1/4 o por 3/4. Otra forma más sencilla es hacer una muesca en el disco, que es la solución que hemos usado.

## Materiales usados en la práctica
El principal componenente que hemos utilizado ha sido el [optointerruptor ITR8102](https://github.com/clases-julio/p4-encoderoptico-rsanchez2021/blob/main/ITR8102-datasheet.pdf). este modelo incorpora un LED infrarrojo y un fototransistor [NPN](https://www.arrow.com/es-mx/categories/optoelectronics/photoelement/phototransistors).

Se ha utilizado además un sistema divisor de voltaje porporcionado por el profesor para el transistor para que tanto la entrada como la salida del transistor y de la placa correspondadn con los voltajes que aceptan. Las resistencias que se han utilizado son de 10KΩ 20KΩ y 330Ω. El diagrama proporcionado es el siguiente:

![Divisor de voltaje](https://github.com/rsanchez2021/Image/blob/main/Captura%20desde%202022-11-21%2013-40-42.png)

También, se ha utilizado un [motor dc](https://harmonicdrive.de/es/glosario/motor-dc) para hacer girar una rueda con muescas:

![Rueda empelada p4](https://github.com/rsanchez2021/Image/blob/main/Captura%20desde%202022-11-21%2013-48-13.png)

Finalmente, se ha empleado el soporte para la rueda creado por Diego García y Ioana Pasca:

![Soporte 1 p4](https://github.com/rsanchez2021/Image/blob/main/Captura%20desde%202022-11-21%2013-48-48.png) ![Soporte 2 p4](https://github.com/rsanchez2021/Image/blob/main/Captura%20desde%202022-11-21%2013-49-01.png)

finalmente: el circuito queda de la siguiente manera:

AÑADIR FOTO DEL FRIZTING DEL CIRCUITO CON MOTOR INCLUIDO


## Ejercicio

Para este ejercicio hemos tenido que emplear lo aprendido en la p3 sobre los eventos. La función principal es un add_event_detecr que va contando los pulsos para después, con una fórmula, sacar las revoluciones por minuto (rpm) del motor. 

Lo que más nos ha costado de esta práctica es sin duda montar el circuito. Al principio queríamos utilizar un [amplificador operacional](https://www.diarioelectronicohoy.com/blog/el-amplificador-operacional) para conectar el motor y poder utilizarlo durante tiempos fijos, pero en el kit proporcionado no contábamos con ninguno que tuviese una señal **enable** para poder controlarlo desde la placa. Para solucionar esto, lo más sencillo y práctico era conectar directamente el motor a la placa junto con un pulsador para activarlo cuando queramos.

Finalmente, el tema de crear el circuito también nos ha costado pues no terminábamos de comprender el divisor de voltaje.




