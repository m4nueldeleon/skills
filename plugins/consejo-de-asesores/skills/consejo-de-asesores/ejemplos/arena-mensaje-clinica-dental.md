# Ejemplo · Modo arena · Mensaje de WhatsApp para una clínica dental

> Negocio de ejemplo (ficticio). Conversación producida siguiendo la skill al pie de la letra.

**Tú:** Arena: necesito un mensaje de WhatsApp para los pacientes que no han venido a su limpieza en más de
8 meses. Esto me dio la IA y suena a robot:
"Estimado paciente: Esperamos que este mensaje lo encuentre bien. En Clínica Dental Los Pinos nos
preocupamos por su salud bucal. Le recordamos que es importante realizarse una limpieza dental cada seis
meses para prevenir enfermedades graves. No dude en contactarnos para agendar su cita. ¡Lo esperamos!"

**Claude:** Va. Antes de ponerlas a competir: ¿qué quieres que haga el paciente después de leerlo? Por
ejemplo: que conteste para agendar, que llame o que entre a un link.

**Tú:** Que contesten y agenden su limpieza. Ojalá con un número o algo fácil.

**Claude:** ¿Hay algún dato que tenga que ir sí o sí? Por ejemplo: quién lo firma, horarios, precio o
condiciones.

**Tú:** Lo manda Rosa, la recepcionista. La doctora es la Dra. Laura. Tengo lugares los sábados de 9 a 2 y
la limpieza dura como 45 minutos. Con seguro, a muchos les sale sin costo o casi; sin seguro son 95 dólares.
No hay promoción.

**Claude:** Va la arena. Hago 4 versiones y no 100: cada versión gasta parte del uso de tu cuenta de Claude,
y después de 4 o 5 bien distintas, las nuevas ya se parecen entre sí. Lo que hace ganar es que sean de
verdad distintas y que los criterios estén claros desde antes.

La ganadora mejorada va al final, lista para copiar.

### Los criterios (del 1 al 5)

| Criterio | Qué mide | Peso |
|---|---|---|
| Suena a persona | Que no parezca robot: es justo lo que no te gustó del primero | ×2 (el más importante) |
| Pide una sola cosa | Que quede claro qué contestar, y que contestar cueste un segundo | ×2 |
| Es de tu clínica | Rosa, la doctora, los sábados: que no pueda ser de cualquier consultorio | ×1 |
| Honesto y sin regaño | Que no asuste, no regañe, no prometa costos que dependen del seguro y no invente nada | ×1 |
| Largo justo | Que se lea en WhatsApp sin bajar la pantalla | ×1 |

Total posible: 35.

### La que hay que vencer (Versión 0)

> Estimado paciente: Esperamos que este mensaje lo encuentre bien. En Clínica Dental Los Pinos nos
> preocupamos por su salud bucal. Le recordamos que es importante realizarse una limpieza dental cada seis
> meses para prevenir enfermedades graves. No dude en contactarnos para agendar su cita. ¡Lo esperamos!

### Los contendientes

**A · Al grano**

> Hola, [nombre]. Soy Rosa, de Clínica Dental Los Pinos. Ya le toca su limpieza: la última fue hace más de
> 8 meses. Los sábados tenemos lugar de 9 a 2 y dura unos 45 minutos. ¿Le aparto uno? Contésteme 1 si
> prefiere temprano (9 a 11) o 2 si prefiere más tarde (11 a 2).

**B · De confianza**

> Hola, [nombre]. Le saluda Rosa, de Los Pinos. La Dra. Laura me pidió preguntarle cómo ha estado, porque
> hace rato que no nos visita. Cuando quiera ponerse al día con su limpieza, los sábados tenemos lugar de 9
> a 2. Nomás contésteme con un 1 y le busco el horario que mejor le quede.

**C · La objeción primero**

> Hola, [nombre]. Soy Rosa, de Clínica Dental Los Pinos. Sabemos que entre semana casi no hay tiempo, por
> eso los sábados atendemos de 9 a 2. Su limpieza toma unos 45 minutos, y con muchos seguros dentales sale
> sin costo o casi. ¿Le aparto un lugar? Contésteme SÍ y le mando los horarios libres.

**D · La mínima**

> Hola, [nombre], soy Rosa de Clínica Dental Los Pinos. Ya le toca su limpieza. ¿Le aparto un lugar este
> sábado? Contésteme 1 y le paso los horarios.

### Ronda de calificación

| Versión | Suena a persona ×2 | Pide una sola cosa ×2 | Es de tu clínica | Honesto y sin regaño | Largo justo | Total |
|---|---|---|---|---|---|---|
| 0 · La original | 1 | 2 | 2 | 2 | 3 | **13** |
| A · Al grano | 4 | 5 | 4 | 3 | 4 | **29** |
| B · De confianza | 5 | 4 | 5 | 3 | 4 | **30** |
| C · La objeción primero | 4 | 4 | 5 | 3 | 3 | **27** |
| D · La mínima | 4 | 5 | 3 | 4 | 5 | **30** |

**0 · La original**
- Lo mejor: nombra la clínica.
- Lo peor: «Esperamos que este mensaje lo encuentre bien» y «No dude en contactarnos» suenan a robot, y
  «para prevenir enfermedades graves» asusta.

**A · Al grano**
- Lo mejor: «Contésteme 1 si prefiere temprano… o 2 si prefiere más tarde». Contestar cuesta un segundo.
- Lo peor: «Ya le toca su limpieza: la última fue hace más de 8 meses». Suena a reclamo.

**B · De confianza**
- Lo mejor: «me pidió preguntarle cómo ha estado». Suena a alguien que se acuerda del paciente.
- Lo peor: «La Dra. Laura me pidió…». Si no es cierto, es un dato inventado. Y la acción llega hasta la
  última línea.

**C · La objeción primero**
- Lo mejor: «Sabemos que entre semana casi no hay tiempo». Se adelanta a la excusa más común.
- Lo peor: «con muchos seguros dentales sale sin costo o casi». Promete algo que depende del plan de cada
  paciente. Y «por eso los sábados atendemos» da una razón que quizá no es la real.

**D · La mínima**
- Lo mejor: «¿Le aparto un lugar este sábado?». Una pregunta, una respuesta.
- Lo peor: «Ya le toca su limpieza». Es un poco de regaño, y nada la distingue de otra clínica.

### La final: B contra D

B tiene lo que le falta a D: calidez y detalles de tu clínica (la doctora, el horario de 9 a 2). D tiene lo
que le falta a B: va directo a la pregunta y no trae nada que haya que verificar. Empatan en 30. Gana B
porque saca más en «Suena a persona», el criterio más importante. Para mejorarla hay que quitarle la frase
que podría ser inventada y traer la pregunta de D.

## La ganadora (lista para copiar)

```text
Hola, [nombre]. Le saluda Rosa, de Clínica Dental Los Pinos, de parte de la Dra. Laura. Hace rato que no nos visita y queremos saber cómo ha estado. Si quiere ponerse al día con su limpieza, los sábados tenemos lugar de 9 a 2 (son unos 45 minutos). ¿Le aparto uno? Contésteme con un 1 y le busco el horario.
```

**Calificación final:** 34 de 35. Suena a persona 5, Pide una sola cosa 5, Es de tu clínica 5, Honesto y
sin regaño 5, Largo justo 4. En largo no mejoró: sigue ocupando cinco renglones en el celular.
**Por qué ganó:** es la única que suena a una persona de la clínica que se acuerda del paciente, sin
regañarlo ni asustarlo. Ahora además termina con una pregunta que se contesta con un número.
**Qué le pusimos de las otras:** la pregunta «¿Le aparto uno?» de D y los 45 minutos de A.
**Antes de mandarlo:**
- Cambia [nombre] por el nombre de cada paciente y mándalo uno por uno, no en un grupo.
- Confirma que los sábados de 9 a 2 sigan libres.
- Pregúntale a la Dra. Laura si está de acuerdo en que la mencionen.
- Si alguien pregunta por el costo, que Rosa revise su seguro antes de prometer que sale gratis.
- No pongas en el mensaje nada del tratamiento del paciente.

**Si quieres probarlo en la vida real:** manda la ganadora a la mitad de tus pacientes y la D a la otra
mitad. Compara cuántos contestan con un 1 en una semana.

¿Seguimos? Puedes escribir «otra arena» (versiones con estrategias nuevas), «cambia el criterio [x]» o «más
corta».
