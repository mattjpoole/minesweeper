# minesweeper
Minesweeper clone using PyGame

TODO:

1. ~Win state~
   * ~check for all flags correctly placed~
   * ~cannot place more flags than mines~
   * ~win screen~
   * ~make win screen text sensitive to new hiscore~
   * ~cell hover disabled while open~
2. ~Game over state~
   * ~detect when all mines are revealed~
   * ~stop timer~
   * ~show game over screen~
3. High scores - save best times for each level - show high scores
   * ~create and save data structure~
   * ~update on better times~
   * ~show high score in end screen~
   * ~prettify hiscore list~
   * highlight hiscore box on new hiscore
   * ~disable drop down when on end screen~
4. Executables https://pyinstaller.org/en/stable/index.html
   * ~Windows~
   * Mac
5. ~Improve empty square colour, make alternating light/dark~
6. ~Sweeper field should not react under open drop down~
7. ~Refactor main.py~
8. Be more juicy; audio/particle effects
   * Particles on mine on game over
   * ~Particles on flag on game win~
   * sfx on click cell
   * sfx on reveal
   * sfx on place flag
   * sfx on click on mine
   * sfx with mine particles
   * sfx with flag particles
9. ~Theme the drop down menu~
10. ~Prevent first square from ever being a mine~