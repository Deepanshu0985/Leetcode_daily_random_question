class Solution:
    # A = ½ |x₁(y₂ - y₃) + x₂(y₃ - y₁) + x₃(y₁ - y₂)|
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = float('-inf')
        n = len(points)
        for i in range (n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                for k in range(j+1,n):
                    x3,y3 = points[k]
                    temp = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2
                    area = max(area,temp)
        return area


            

        