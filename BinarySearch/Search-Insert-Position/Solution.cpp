int searchInsert(vector<int>& arr, int m)
{
	int start = 0;
	int end = arr.size() - 1;
	int mid = start + (end- start)/2;

	while(start<=end){
		if(arr[mid]==m){
			return mid;
		}
		else if(arr[mid]>m){
			end = mid -1;
		}
		else{
			start =mid+ 1;
		}
		mid = start + (end- start)/2;
	}
	return start;
}