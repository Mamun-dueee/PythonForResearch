region_cols = []## ENTER CODE HERE! ##
for i in whisky.Region:
    region_cols.append(region_colors[i])
    
classification_cols = []## ENTER CODE HERE! ##
for i in whisky.Group:
    classification_cols.append(cluster_colors[i])

location_plot("Whisky Locations and Regions", region_cols)
location_plot("Whisky Locations and Groups", classification_cols)
