# csgo_api
And API for all the weapons in Counter Strike Global Offensive 

*this is still a work in progress*

## How to Use
To use API put weapon in url after version number  
Example: `/api/v0.1/p250' would return
```
{
  "id": "3", 
  "name": "p250", 
  "stats": {
    "accurate_range": "19m", 
    "caliber": ".375", 
    "kill_award": "$300", 
    "mag": "13/52", 
    "movement_speed": "240", 
    "origin": "Germany and Switzerland", 
    "price": "$300", 
    "reload_time": "2.2 seconds", 
    "rof": "400 RPM", 
    "used_by_ct": "yes", 
    "used_by_t": "yes"
  }
}
```
