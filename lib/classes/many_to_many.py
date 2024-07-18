class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    # Name property
    def get_name(self):
        return self._name
    def set_name(self,value):
        # print("attripute exists? ",hasattr(self, "name"))
        if type(value) is str and 3<= len(value) and not hasattr(self, "name"):
            self._name = value
        else:
            print("Not valid name/ cannot change")
    name = property(get_name,set_name)

    def trips(self):
        # Look through all the trips Trip.all
        # IF trips national park is myself
        my_trips = []
        for trip in Trip.all:
            if trip.national_park == self:
                my_trips.append(trip)
        return my_trips
    
    def visitors(self):
        my_visitors = []
        # Look through all the trips, find all of my trips
        # Look through and add each visistor only once
        # If visitor is in list, do nothing, if it isn't add visitor
        for trip in Trip.all:
            if trip.national_park == self and trip.visitor not in my_visitors:
                my_visitors.append(trip.visitor)
        return my_visitors
    
    def total_visits(self):
        my_trips = self.trips()
        return len(my_trips)
    
    def best_visitor(self):
        vistor_dict = {}
        # Loop through all trips
        for trip in Trip.all:
            if trip.national_park == self:
                # if visitor has been seen, +1 to the dict
                if vistor_dict.get(trip.visitor):
                    vistor_dict[trip.visitor] += 1
                # if vistor has not been seen, add to dict
                else:
                    vistor_dict[trip.visitor] = 1
        print(vistor_dict)

        max_visitor = None
        max_visits = 0
        for visitor in vistor_dict:
            if vistor_dict[visitor] > max_visits:
                max_visits = vistor_dict[visitor]
                max_visitor = visitor
        return max_visitor



class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
    
    def get_start_date(self):
        return self._start_date
    def set_start_date(self,value):
        # Split the value up by spaces
        if type(value) is str:
            valid_months = ("January","Febuary","March","April","May")
            date=value.split()
        if type(value) is str and len(value) >= 7 and len(date)==2 and date[0] in valid_months and 3<= len(date[1]) <=4:
            self._start_date= value
        else:
            print("Not valid start date")
    start_date=property(get_start_date,set_start_date)

    def get_end_date(self):
        return self._end_date
    def set_end_date(self,value):
        # Split the value up by spaces
        if type(value) is str:
            valid_months = ("January","Febuary","March","April","May")
            date=value.split()
        if type(value) is str and len(value) >= 7 and len(date)==2 and date[0] in valid_months and 3<= len(date[1]) <=4:
            self._end_date= value
        else:
            print("Not valid end date")
    end_date=property(get_end_date,set_end_date)

    def get_visitor(self):
        return self._visitor
    def set_visitor(self,value):
        if type(value) is Visitor:
            self._visitor = value
        else:
            print("Not valid visitor")
    visitor = property(get_visitor,set_visitor)

    def get_national_park(self):
        return self._national_park
    def set_national_park(self,value):
        if type(value) is NationalPark:
            self._national_park = value
        else:
            print("Not valid national_park")
    national_park = property(get_national_park,set_national_park)

class Visitor:
    all = []
    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)
    
    def get_name(self):
        return self._name
    def set_name(self,value):
        if type(value) is str and 1<= len(value) <= 15:
            self._name = value
        else:
            print("Not valid name")
    name = property(get_name,set_name)
        
    def trips(self):
        my_trips = []
        for trip in Trip.all:
            if trip.visitor == self:
                my_trips.append(trip)
        return my_trips
    
    def national_parks(self):
        my_parks = []
        for trip in Trip.all:
            if trip.visitor == self and trip.national_park not in my_parks:
                my_parks.append(trip.national_park)
        return my_parks
    
    def total_visits_at_park(self, park):
        count = 0
        # loop through all visits (for this visitor)
        my_trips = self.trips()
        # if that vist.parks = park increase a count
        for trip in my_trips:
            if trip.national_park == park:
                count +=1
        return count

    def __repr__(self):
        return self.name