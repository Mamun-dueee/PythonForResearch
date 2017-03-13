(predictors, outcomes) = generate_synth_data()

k = 5; filename = "knn_synth_5.pdf"; limits = (-3, 4, -3, 4); h = 0.1
(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)
plot_prediction_grid(xx, yy, prediction_grid, filename)

