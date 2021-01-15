from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    pokemon_id = models.IntegerField(unique=True, blank=False, primary_key=True)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    hp = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    specialAttack = models.IntegerField(default=0)
    specialDefense = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    evolutions = models.ManyToManyField("self", symmetrical=False, related_name="%(app_label)s_%(class)s_related")
    preEvolution = models.ManyToManyField("self", symmetrical=False)

    def __str__(self):
        return '%d: %s' % (self.pokemon_id, self.name)
