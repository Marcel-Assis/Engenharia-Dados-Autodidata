# Criando uma Função de Gestão de Logs

def custom_logger(level, message):
    import logging
    logger = logging.getLogger(__name__)
    if not (len(logger.handlers)):
        logging.basicConfig(level=logging.INFO)
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler("file.log") # Criação do arquivo file.log na pasta
        format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") # setando o formato do log
        c_handler.setFormatter(format) # atribuindo o formato do log
        f_handler.setFormatter(format) # atribuindo o formato do log
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

    if level == 'debug':
        logger.debug(message)
    elif level == 'info':
        logger.info(message)
    elif level == 'warning':
        logger.warning(message)
    elif level == 'error':
        logger.error(message)
    elif level == 'critical':
        logger.critical(message)

custom_logger("warning", "Atenção, parâmetro errado!") # testando
custom_logger("error", "Parâmetro errado!") # testando

# Utilizando log + gestão de exceções

custom_logger('info', 'início do programa')
lista = [1,2,3]
try:
    print(lista[10])
except:
    custom_logger('error', 'indice incorreto')

custom_logger('info', 'fim do programa')