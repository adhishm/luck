# luck
Experiments on the role of luck in our achievements. This was following the video on this topic by Veritasium: [Is Success Luck or Hard Work?](https://youtu.be/3LopI4YeC4I?si=XVTyc3ISMeWfi1tx).

A population of candidates is generated and they are assigned skill scores and luck scores, each on a normal distribution with mean value 0.5 and standard deviation 0.2. Then, the total score of a candidate is calculated as a weighted sum of the skill and luck scores, with the skill to luck weight ration being 0.95:0.05. In a selection process, a pre-defined number of candidates with the highest score is selected. At the end of the process, the distribution of the selected candidates' skill and luck scores are plotted to see if there are any patterns indicating the role of luck in our success.

Two cases are explored here:
- [Constant Skill, Constant Luck](./constant_skill-constant_luck.ipynb): Candidates' skill and luck scores are generated in the beginning, and remain constant. Two sub-cases are explored here: single round of selection, and multiple rounds of selection with decreasing number of selected candidates
- [Constant Skill, Variable Luck](./constant_skill-variable_luck.ipynb): Candidates' skill scores are generated at the beginning, but the luck scores are regenerated at each selection round (to mimic real-world effects like having a bad day, etc.). Multiple rounds of selection are carried out (single round is the same as constant skill, constant luck for one round)


