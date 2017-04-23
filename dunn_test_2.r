library("clValid")

# Generate some fake data
npoints=1000

x1 <- rnorm(npoints,0,1)
y1 <- 1.2*x1-2++rnorm(npoints,0,1)

x2 <- rnorm(npoints,0,1) + 3.5 
y2 <- -1*x2+rnorm(npoints,0,1)

plot(c(x1,x2), c(y1,y2), pch=20)
express <- data.frame(x = c(x1, x2), y = c(y1, y2))

## hierarchical clustering
Dist <- dist(express,method="euclidean")
clusterObj <- hclust(Dist, method="average")
nc <- 2 ## number of clusters      
cluster <- cutree(clusterObj,nc)
dunn_cl2 <- dunn(Dist, cluster)

nc <- 1 ## number of clusters      
cluster <- cutree(clusterObj,nc)
dunn_cl1 <- dunn(Dist, cluster)

print(dunn_cl1)
print(dunn_cl2)
