# EvolAcc

## Introduction 
EvolAcc aims to be a life simulator based on programmable replicator unit inside a N dimensions world.
EvolAcc provides a powerful API for creation and management of simulation, that allow user to create complex systems.
Moreover, EvolAcc is totally extendable and provides tools for simplify observation and analysis of simulations.

## Dependencies
EvolAcc uses Python 3 and some pip installable python modules:
- docopt  

See *requirements.txt* file for more info.  
Pip allow quick installation of all modules with :

        pip install -r requirements.txt

Careful: on some systems (those use python 2 by default), *pip3* must be used instead of *pip*.

## License 
MIT. See LICENSE file.


## Versions
EvolAcc use the *SemVer* naming for versionning.  
All versions with changelog are described here:
API can drastically change while in Beta. (<1.0.0)

### Planned for next versions
- more doc;
- dynamic genomes;
- Qt GUI;
- more doc;
- more actions, watchers, genomes;
- more tests;
- pypi upload;
- improve config module implementation, because its hard to add an option now;

### 0.2.0
Current version. 
- includes Alterators as modulable component;

### 0.1.0
Stable version. 
- implementation of main architecture;
- provides some objects for API;
- basic objects like some actions, and Game of Life implementation;



