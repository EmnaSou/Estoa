# language: es

Característica: Finalizar el juego con un jaque mate
  Como jugador de ajedrez,
  Quiero que el juego termine con un jaque mate,
  Para seguir las reglas reales del ajedrez.

  Escenario: Jaque mate al rey
    Dado que un jugador pone al rey del oponente en jaque mate
    Cuando no hay movimientos legales para el rey
    Entonces la partida debe terminar
    Y se debe declarar al jugador como ganador.


Característica: Limitar movimientos cuando se está en jaque
  Como jugador de ajedrez,
  Quiero estar limitado solo a movimientos que me saquen del jaque,
  Para jugar según las reglas oficiales del ajedrez.

  Escenario: Jugador en jaque intenta mover
    Dado que un jugador está en jaque
    Cuando intenta hacer un movimiento
    Entonces solo los movimientos que resuelven el jaque son permitidos.


Característica: Piezas que adoptan movimientos de piezas adyacentes
  Como jugador de ajedrez,
  Quiero que una pieza pueda adoptar temporalmente los movimientos de una adyacente,
  Para añadir más estrategia al juego.

  Escenario: Pieza adquiere nuevos movimientos
    Dado que una pieza es seleccionada
    Cuando está adyacente a otra pieza con movimientos diferentes
    Entonces puede adquirir y utilizar los movimientos de la pieza adyacente temporalmente.