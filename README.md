## Take home exercise for Fetch

Challenge
1. Play around with the website and find the best algorithm (minimum number of weighings for any possible
fake bar position) to find the fake gold bar.
2. Create the test automation project using any preferred language to perform
   - Clicks on buttons (“Weigh”, “Reset”)
   - Getting the measurement results (field between the 'bowls')
   - Filling out the bowls grids with bar numbers (0 to 8)
   - Getting a list of weighing
   - Clicking on the gold bar number at the bottom of the website and checking for the alert message
4. Code the algorithm from step 1 which uses a set of actions from step 2 to find the fake gold bar
The algorithm should populate and weigh gold bars until a fake on


## My Algorithm

1. Put the bars in three different groups
2. Weigh Group 1 against Group 2:
   - If they are balanced, then Group 3 must have the fake bar
   - If the are not balanced, the lighter group will have the fake bar
3. Divide the remaining three bars, and measure Bar 1 against Bar 2:
   - If they are balanced, then then Bar 3 must have the fake bar
   - If they are not balanced, then the lighter bar is the fake bar
  
     
