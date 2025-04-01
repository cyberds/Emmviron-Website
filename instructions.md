## to see all the containers in docker
docker-compose ps


## backup database using docker
`docker exec -t emmviron-website-db-1 pg_dump -U neondb_owner -F c neondb > db_backups/backup.dump`

## to restore database using docker
`docker exec -i emmviron-website-db-1 pg_restore -U neondb_owner -d neondb < db_backups/backup.dump`

## Django commands with docker
To run commands, you must add `docker-compose exec web` before the command.

### example
`docker-compose exec web python manage.py migrate`