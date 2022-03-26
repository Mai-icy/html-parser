from scheduler import schedule, run

def person(name, count):
  for i in range(count):
    print(name, "running")
    yield

schedule(person("John", 2))
schedule(person("Michael", 3))
schedule(person("Terry", 4))

run()
