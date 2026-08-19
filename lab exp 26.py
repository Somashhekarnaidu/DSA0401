import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
df = pd.read_csv("clinical_trial.csv")
control = df[df["Group"] == "Control"]["Effect"]
treatment = df[df["Group"] == "Treatment"]["Effect"]
t_stat, p_value = ttest_ind(control, treatment)
print("Control Group Mean:", control.mean())
print("Treatment Group Mean:", treatment.mean())
print("T-statistic:", t_stat)
print("P-value:", p_value)
alpha = 0.05
if p_value < alpha:
    print("Result: Reject the null hypothesis.")
    print("The treatment has a statistically significant effect.")
else:
    print("Result: Fail to reject the null hypothesis.")
    print("The treatment does not have a statistically significant effect.")
plt.figure(figsize=(8, 5))
plt.boxplot(
    [control, treatment],
    labels=["Control", "Treatment"]
)
plt.ylabel("Treatment Effect")
plt.title("Clinical Trial: Control vs Treatment")
plt.text(
    1.5,
    max(df["Effect"]) + 1,
    f"p-value = {p_value:.4f}",
    ha="center"
)
plt.grid(axis="y", alpha=0.3)
plt.show()
