# Simple-Hackpad
Just a simple Hackpad with 3 switches, an OLED screen, and rotary encoder. It was built as part of the [Hack Club Hackpad YSWS](https://hackpad.hackclub.com/)

![Simple Hackpad](https://media.printables.com/media/prints/86d3d299-cbb3-4c33-a3d0-99e86b7bdbce/images/13097328_8c6fe636-a239-4a10-a60a-6fe8b14e755e_f1bdefcd-b82a-4a2f-8229-e88218483361/thumbs/cover/800x800/png/macropad.png)

**[View on Printables →](https://www.printables.com/model/1747786-simple-hackpad)**

## Features

- 3 mechanical key switches
- EC11 Rotary encoder
- 128x32 OLED display
- Seeed XIAO RP2040 microcontroller
- Made in Onshape, PCB designed in KiCad

## Case & CAD

![Empty Case](https://media.printables.com/media/prints/43b99499-ae65-4e42-99f8-a67c36ecdc79/images/13097329_3c8e2281-b7e7-496e-a97c-95127c218e7d_cd46ae90-b841-4db6-b4f4-10dd7de5194d/thumbs/cover/800x800/png/empty-case.png)

The case is a simple two-piece print. It is a base where the PCB sits, and a top cover. Everything slides together.

Designed in Onshape.

## PCB

![Schematic](https://media.printables.com/media/prints/3e827a9f-bcbc-440e-a166-6f9890aaa3b7/images/13097330_71cc7e9e-a7e1-4889-aa95-1a7bc21c802c_09692905-ffdd-4694-925a-a935c675540c/thumbs/cover/800x800/png/schematic.png)

![PCB](https://media.printables.com/media/prints/7dbaccdd-9f08-403d-a9bf-83a70ec09853/images/13097331_219b6001-b7fd-4cb1-a356-d365630dfb6c_35ae452d-250b-45dc-9c27-4bab0509dfbc/thumbs/cover/800x800/png/schematyic.png)

The PCB was designed in KiCad. Key switch footprints use MX_V2. The OLED and rotary encoder connect directly to the XIAO via I2C and GPIO.

## Firmware

This hackpad runs [KMK](https://kmkfw.io/) firmware on the XIAO RP2040.

- The 4 keys act as customizable macros
- The rotary encoder can be mapped to volume, scroll, zoom, or anything else

## Bill of Materials

| Part | Qty |
|------|-----|
| Cherry MX Switches | 3 |
| Keycaps (DSA or similar) | 3 |
| EC11 Rotary Encoder + knob | 1 |
| 0.91" 128x32 OLED Display | 1 |
| Seeed XIAO RP2040 | 1 |
| 3D Printed Case | 1 set |

## Credits

- Inspired by [Orpheuspad](https://github.com/hackclub/hackpad) and the Hack Club Hackpad YSWS
- Case designed in Onshape
- PCB designed in KiCad
- Firmware: [KMK](https://kmkfw.io/)
