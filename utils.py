class Utils():

    def __init__(self) -> None:
        pass

    def milliseconds_to_display_text(self, milliseconds) -> str:
        total_time_in_seconds = int(milliseconds / 1000)
        seconds = int(total_time_in_seconds % 60)
        minutes = int(total_time_in_seconds / 60)
        display_seconds = str(seconds)
        if (seconds<10):
            display_seconds = "0"+display_seconds
        display_minutes = str(minutes)
        if (minutes<10):
            display_minutes = "0"+display_minutes
        return display_minutes+":"+display_seconds