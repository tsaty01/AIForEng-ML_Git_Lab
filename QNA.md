1. **Why is version control important in ML projects?**

   Version control is essential in machine learning because it ensures reproducibility. Unlike standard software, ML involves code, data, and hyperparameters. If you don't track the exact state of the code that produced a specific model, you can't reproduce the results later. It also allows for safe experimentation (testing different algorithms on separate branches without breaking the main code) and enables smooth collaboration so team members working on preprocessing or training don't overwrite each other's changes.

2. **What problems occur if Git is not used?**

   Without Git, you lose the project history, meaning you can't revert to a working version if a new change (like a bad hyperparameter) breaks the model. It also leads to collaboration conflicts, where merging work between team members becomes a manual, error-prone mess. Finally, there is no traceability, so it’s hard to figure out which script version generated a specific model result.

3. **Why should datasets and trained models be handled carefully in Git?**

   Standard Git is built for text and code, not large binary files. Committing heavy files like .csv datasets or .pkl models causes repository bloat, making cloning and fetching painfully slow. Also, platforms like GitHub have strict file size limits (usually 100MB). It is best practice to use tools like Git LFS for these files and only keep lightweight code in the main Git history.
