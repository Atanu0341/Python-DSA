int lowerBound(vector<int> arr, int n, int x) {
	// Write your code here
	if(arr[0]>=x){
        return 0;
    }
	else if(arr[n-1]<x){
        return n;
    }

	int start = 0;
	int end = n-1;
	
	int mid = start + (end - start)/2;

	while(start<=end){

		if(arr[mid]==x){
			return mid;
		}
		else if(arr[mid]<x){
			start = mid + 1;
		}
		else{
			end = mid - 1;
		}
		mid = start + (end - start)/2;
	}
	return start;
}
