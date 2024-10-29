import data

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1:data.Point, point2: data.Point) -> data.Rectangle:
    if point1.x < point2.x and point1.y > point2.y:
        top_left = point1
        bottom_right = point2
        rectangle = data.Rectangle(top_left, bottom_right)
        return rectangle
    elif point1.x > point2.x and point1.y < point2.y:
        top_left = point2
        bottom_right = point1
        rectangle = data.Rectangle(top_left, bottom_right)
        return rectangle
    elif point1.x < point2.x and point1.y < point2.y:
        top_left = data.Point(point1.x, point2.y)
        bottom_right = data.Point(point2.x, point1.y)
        rectangle = data.Rectangle(top_left, bottom_right)
        return rectangle
    elif point1.x > point2.x and point1.y > point2.y:
        top_left = data.Point(point2.x, point1.y)
        bottom_right = data.Point(point1.x, point2.y)
        rectangle = data.Rectangle(top_left, bottom_right)
        return rectangle
# Part 2
def shorter_duration_than(duration1:data.Duration, duration2:data.Duration) -> bool:
    if duration1.minutes < duration2.minutes:
        return True
    elif(duration1.minutes == duration2.minutes and duration1.seconds < duration2.seconds):
        return True
    else:
        return False

# Part 3
def song_shorter_than(song_list:list[data.Song],upper_bound:data.Duration) -> list[data.Song]:
    new_list = []
    for song in song_list:
        if song.duration.minutes < upper_bound.minutes:
            new_list.append(song)
        elif song.duration.minutes == upper_bound.minutes and song.duration.seconds < upper_bound.seconds:
            new_list.append(song)
    return new_list

# Part 4
def running_time(song_list:list[data.Song],int_list:list[int]) -> data.Duration:
    total_time = data.Duration(0,0)
    for num in int_list:
        if(song_list[num].duration.seconds+total_time.seconds >=60):
            total_time.minutes+=1
            total_time.seconds = (total_time.seconds + song_list[num].duration.seconds)%60
        else:
            total_time.seconds += song_list[num].duration.seconds
        total_time.minutes+=song_list[num].duration.minutes
    return total_time



# Part 5
def validate_route(city_links:list[list[str]], route:list[str]) ->bool:
    bool = True
    if(len(route)==2):
        if([route[0],route[1]] in city_links):
            bool = True
        else:
            bool = False
    else:
        for idx in range(len(route)-2):
            if(([route[idx],route[idx+1]] in city_links)):
                bool = True
            elif (route == []):
                bool = True
            else:
                bool = False

    return bool
# Part 6
def longest_repetition(the_list:list[int])->int:
    count = 0
    longest_streak = 0
    streak_idx = 0
    for idx in range(1,len(the_list)):
        if(the_list[idx] == the_list[idx-1]):
            count += 1
        elif count > longest_streak:
            longest_streak = count
            streak_idx = idx-count-1
            count = 0
        else:
            count = 0
    return streak_idx