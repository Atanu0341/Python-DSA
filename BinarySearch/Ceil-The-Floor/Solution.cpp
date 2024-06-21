

int findFloor(vector<int> &a, int n, int x) {
  int start = 0;
  int end = n - 1;
  int ans = -1;

  while (start <= end) {
    int mid = start + (end - start) / 2;
    if (a[mid] <= x) {
      ans = a[mid];
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  return ans;
}

int findCeil(vector<int> &a, int n, int x) {
  int start = 0;
  int end = n - 1;
  int ans = -1;

  while (start <= end) {
    int mid = start + (end - start) / 2;
    if (a[mid] >= x) {
      ans = a[mid];
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return ans;
}

pair<int, int> getFloorAndCeil(vector<int> &a, int n, int x) {
  pair<int, int> p;

  p.first = findFloor(a, n, x);
  p.second = findCeil(a, n, x);

  return p;
}
