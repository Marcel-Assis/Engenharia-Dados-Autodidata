def custom_logger(level, message): # Função personalizada para configurar o logger e registrar mensagens de log
    import logging # Importa o módulo logging para trabalhar com logs
    logger = logging.getLogger(__name__) # Obtém um logger específico para o módulo atual usando o nome do módulo como identificador
    if not (len(logger.handlers)): # Verifica se o logger já possui handlers configurados para evitar configurações duplicadas
        logging.basicConfig(level=logging.INFO) # Configura o nível de log para INFO, o que significa que mensagens de INFO e níveis superiores serão registradas
        c_handler = logging.StreamHandler() # Cria um handler para enviar logs para o console
        f_handler = logging.FileHandler('file.log') # Cria um handler para enviar logs para um arquivo chamado 'file.log'
        format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # Define o formato das mensagens de log, incluindo a data e hora, nome do logger, nível de log e a mensagem
        c_handler.setFormatter(format) # Aplica o formato definido ao handler do console
        f_handler.setFormatter(format) # Aplica o formato definido ao handler do arquivo
        logger.addHandler(c_handler) # Adiciona o handler do console ao logger para que as mensagens de log sejam exibidas no console
        logger.addHandler(f_handler) # Adiciona o handler do arquivo ao logger para que as mensagens de log sejam gravadas no arquivo 'file.log'

    # Registra a mensagem de log com base no nível especificado
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
    
    # Exemplo de uso da função custom_logger
custom_logger('info', 'Esta é uma mensagem de log personalizada.') # Chama a função custom_logger para registrar uma mensagem de log com o nível INFO e a mensagem "Esta é uma mensagem de log personalizada."
custom_logger('error', 'Esta é uma mensagem de erro personalizada.') # Chama a função custom_logger para registrar uma mensagem de log com o nível ERROR e a mensagem "Esta é uma mensagem de erro personalizada."
custom_logger('debug', 'Esta é uma mensagem de depuração personalizada.') # Chama a função custom_logger para registrar uma mensagem de log com o nível DEBUG e a mensagem "Esta é uma mensagem de depuração personalizada."
custom_logger('warning', 'Esta é uma mensagem de aviso personalizada.') # Chama a função custom_logger para registrar uma mensagem de log com o nível WARNING e a mensagem "Esta é uma mensagem de aviso personalizada."
custom_logger('critical', 'Esta é uma mensagem crítica personalizada.') # Chama a função custom_logger para registrar uma mensagem de log com o nível CRITICAL e a mensagem "Esta é uma mensagem crítica personalizada."
