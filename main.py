from database.migrations import run_migrations

def main():
    run_migrations()
    # dto = UserDTO.create(username='admin', password='admin987654')
    # try: 
    #     dto.validate()
    #     user_service = UserService()
    #     data = user_service.create_user(dto)
    #     print(data)
    # except ValueError as e:
    #     print(e)
    


if __name__ == '__main__':
    main()