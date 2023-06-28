# Use a priority queue to maintain k closest points
# Implemented as a max heap, so we can pop the largest element when the size exceeds k
class Solution0: # O(nlogk) time, O(k) space for pq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for x, y in points:
            dist = x*x + y*y # No need to take the square root, invariant is maintained
            # Add elements to the heap in order of their negative distance.
            # Since heapq uses min heap by default, distance is negated to make it a max heap.
            # We add -dist and point to a tuple so that the heap is ordered by distance
            if len(pq) == k:
                heapq.heappushpop(pq, (-dist, [x, y]))
            else:
                heapq.heappush(pq, (-dist, [x, y]))

        return [point for dist, point in pq] # Strip the distance from the result

class Solution1: # Faster, but such a pain to understand this partitioning algorithm (Note that this is still O(n^2) for worst case, sorted or same values. O(n) on average though?)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def compare(p1, p2): # Compare function, returns difference in distance to origin
            return (p1[0]*p1[0] + p1[1]*p1[1]) - (p2[0]*p2[0] + p2[1]*p2[1])

        # Helper partitions points into two parts, one smaller than pivot and one larger than pivot
        def helper(l, r):
            pivot = points[l] # The first element of the subarray is chosen arbitrarily
            # Rearrange points so that all elements smaller than pivot are to the left of it, and vice versa
            while l<r:
                # In each iteration this is essentially happening:
                #  - Find the first element from the right that is smaller than pivot (r)
                #  - Find the first element from the left that is larger than pivot (l)
                #  - Swap them
                # However we can simplify this. Instead of using a temp for the swap, we can use the last r/l (opposite from whatever is being moved) value as the holding value.
                # This works because the first value written over is actually the pivot, and for following iterations we have an extra space to use as a temp
                # This means that every iteration ends with a duplicate value; points [l] = points[r]
                # See the following example:
                # 
                # l             r   before first iteration
                # 5 9 1 7 2 3 8 4
                #   l           r   after first iteration
                # 4 9 1 7 2 3 8 9   
                #       l   r       after second iteration
                # 4 3 1 7 2 7 8 9
                #         p         third iteration ends because l meets r
                # 4 3 1 2 2 7 8 9
                # Then we can bring the pivot back where it is supposed to be, removing the duplicate value
                # 4 3 1 2 5 7 8 9
                #
                # This is really hard to understand imo, but it's like a delayed swap.
                # To see the swap, note how l is written onto r, and the value ABOVE r (from previous iteration) is duplicated TWO UNDER l (from previous iteration).
                # This makes it clear how l is the holding value, since it gets written into r.
                # This also is clear from the start, since it acts as the pivot sentinel, being overwritten below it whereas once r is written onto that index stays the same.
                # This hopefully makes a little sense as to why points[l] = pivot at the end.
                
                while l<r and compare(points[r], pivot)>=0: r-=1
                points[l] = points[r] # Overwrite the duplicate l with points[r]. In first iteration, it is the pivot rather than duplicate
                while l<r and compare(points[l], pivot)<=0: l+=1
                points[r] = points[l] # Since we wrote points[r] onto the OLD l, we can put the new l into points[r]

            # At the end of these iterations, l meets are r at the pivot point. 
            points[l] = pivot
            return l # Return the pivot point to see how many elements are smaller than it for the problem

        l = 0
        r = len(points) - 1

        while l<=r:
            mid = helper(l, r) # Split points into a part smaller than mid and larger than mid
            if mid == k: break # If there are k points smaller than mid, that is the solution
            if mid<k: # All elements behind mid will be part of result, so just do the same to other elements to get more
                l = mid + 1
            else: # We only know that elements past k won't be in res, so just recurse on the other half
                r = mid - 1

        return points[:k] # Return the first k elements, which will be all elements before the pivot.

        