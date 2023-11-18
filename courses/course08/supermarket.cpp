#include <iostream>

using namespace std;

int main()
{
    int A, B, C;
    cin >> A >> B >> C;
    int K, sum, minRoll, minTime, curTime;

    sum = 0;
    for (int i = 0; i < A; ++i)
    {
        cin >> K;
        sum += K;
    }
    minTime = sum * 3 + (A - 1) * 2;
    minRoll = 1;

    sum = 0;
    for (int i = 0; i < B; ++i)
    {
        cin >> K;
        sum += K;
    }
    curTime = sum * 3 + (B - 1) * 2;
    if (curTime < minTime)
    {
        minTime = curTime;
        minRoll = 2;
    }

    sum = 0;
    for (int i = 0; i < C; ++i)
    {
        cin >> K;
        sum += K;
    }
    curTime = sum * 3 + (C - 1) * 2;
    if (curTime < minTime)
    {
        minTime = curTime;
        minRoll = 3;
    }

    cout << minRoll << " " << minTime << endl;
}