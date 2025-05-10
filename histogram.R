library(ggplot2)

years <- c(2019, 2020, 2021, 2022)
lfp_rate <- c(61.3, 59.5, 63.3, 64.7)
employment_rate <- c(94.9, 89.7, 92.2, 94.6)
underemployment_rate <- c(13.8, 16.2, 15.9, 14.2)
unemployment_rate <- c(5.1, 10.3, 7.8, 5.4)

df <- data.frame(
  Year = rep(years, 4),
  Rate = c(lfp_rate, employment_rate, underemployment_rate, unemployment_rate),
  Category = rep(c("Labor Force Participation Rate", "Employment Rate", 
                   "Underemployment Rate", "Unemployment Rate"), each = 4)
)

ggplot(df, aes(x = Rate, y = as.factor(Year), fill = Category)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8),
           width = 0.7) +
  scale_fill_manual(values = c("skyblue", "green", "orange", "red")) +
  labs(
    title = "Key Labor and Employment Indicators (2019–2022)",
    x = "Rate (%)",
    y = "Year"
  ) +
  theme_minimal() +
  theme(
    legend.position = "top",
    axis.title.y = element_blank(),
    panel.grid.major.y = element_blank(),
    panel.grid.minor.y = element_blank()
  )
ggsave("histogram.png", width = 10, height = 6, dpi = 300)
