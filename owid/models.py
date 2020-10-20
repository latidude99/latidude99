import datetime

from django.db import models
#from django.utils import timezone


class Country(models.Model):
    location = models.CharField(max_length=200)
    continent = models.CharField(max_length=200)
    population = models.FloatField(default=0)
    population_density = models.FloatField(default=0)
    median_age = models.FloatField(default=0)
    aged_65_older = models.FloatField(default=0)
    aged_70_older = models.FloatField(default=0)
    gdp_per_capita = models.FloatField(default=0)
    cardiovasc_death_rate = models.FloatField(default=0)
    diabetes_prevalence = models.FloatField(default=0)
    handwashing_facilities = models.FloatField(default=0)
    hospital_beds_per_thousand = models.FloatField(default=0)
    life_expectancy = models.FloatField(default=0)
    human_development_index = models.FloatField(default=0)

    def __str__(self):
        return self.location



class CovidData(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date = models.DateTimeField('date')
    new_cases = models.FloatField(default=0)
    total_cases = models.FloatField(default=0)
    new_deaths = models.FloatField(default=0)
    total_deaths = models.FloatField(default=0)
    new_cases_per_million = models.FloatField(default=0)
    total_cases_per_million = models.FloatField(default=0)
    new_deaths_per_million = models.FloatField(default=0)
    total_deaths_per_million = models.FloatField(default=0)
    import_date = models.DateTimeField('import date')

    def __str__(self):
        return " " + self.country.location + \
               " " + str(self.date) + \
               " " + str(self.new_cases) + \
               " " + str(self.total_cases) + \
               " " + str(self.new_deaths) + \
               " " + str(self.total_deaths)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'country'], name="unique_date")
            ]