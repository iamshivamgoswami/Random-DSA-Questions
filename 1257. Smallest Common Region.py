class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:

        parents={region[i]:region[0] for region in regions for i in range(1,len(region))}
        history={region2}
        while region2 in parents:
            region2=parents[region2]
            history.add(region2)
        while region1 not in history:
            region1=parents[region1]
        return region1

