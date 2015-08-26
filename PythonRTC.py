#!/usr/bin/python

# PythonRTC - Python Hardware Programming Education Project For Raspberry Pi
# Copyright (C) 2015 Jason Birch
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#/****************************************************************************/
#/* PythonRTC                                                                */
#/* ------------------------------------------------------------------------ */
#/* V1.00 - 2015-08-26 - Jason Birch                                         */
#/* ------------------------------------------------------------------------ */
#/* Example of using class to handle controlling a Real Time Clock IC DS1302.*/
#/****************************************************************************/


# Use the class for the DS1302 RTC chip.
import RTC_DS1302


# Create an instance of the RTC class.
ThisRTC = RTC_DS1302.RTC_DS1302()

# Functions to write to the RTC chip.
ThisRTC.WriteRAM("Message for RAM on RTC DS1302")
ThisRTC.WriteDateTime(15, 8, 26, 3, 20, 59, 30)

# Functions to read from the RTC chip.
Data = ThisRTC.ReadRAM()
print("Message: " + Data)

DateTime = { "Year":0, "Month":0, "Day":0, "DayOfWeek":0, "Hour":0, "Minute":0, "Second":0 }
Data = ThisRTC.ReadDateTime(DateTime)
print("Date/Time: " + Data)
print("Year: " + format(DateTime["Year"] + 2000, "04d"))
print("Month: " + format(DateTime["Month"], "02d"))
print("Day: " + format(DateTime["Day"], "02d"))
print("DayOfWeek: " + ThisRTC.DOW[DateTime["DayOfWeek"]])
print("Hour: " + format(DateTime["Hour"], "02d"))
print("Minute: " + format(DateTime["Minute"], "02d"))
print("Second: " + format(DateTime["Second"], "02d"))

# Finish with the Raspberry Pi GPIO pins.
ThisRTC.CloseGPIO()
