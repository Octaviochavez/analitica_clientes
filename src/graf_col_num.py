# Respaldo de código para gráficos de dispersión entre variables numéricas utilizando seaborn

import seaborn as sns

# Array de variables numéricas para los gráficos de dispersión
numeric_cols = ["edad",	"ingreso_mensual",	"gasto_mensual",	"deuda_total",	"score_crediticio",	"antiguedad_meses",	"frecuencia_compra",	"ultima_compra_dias",	"num_productos",	"hora_registro"]

# Scatter plot matrix más compacto
sns.set(style="ticks", palette="pastel")
pairplot = sns.pairplot(
    data[numeric_cols],
    kind='scatter',
    diag_kind='kde',
    height=1.7
)
pairplot.fig.suptitle("Scatter Plot Matrix de Variables Numéricas", y=1.02)
plt.show()