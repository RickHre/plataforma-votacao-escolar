# Rotas

Health:
* GET /

Auth:
* POST /auth/login    -> Autentica o usuário
* POST /auth/register -> Registra um novo usuário

Users:
* GET    /users           -> Retorna todos os usuários (não cancelados)
* GET    /users/{user_id} -> Retorna o usuário que tenha o {user_id} correspondente
* POST   /users           -> Cria um novo usuário
* PATCH  /users/{user_id} -> Edita um ou mais campos do usuário com {user_id} correspondente
* DELETE /users/{user_id} -> Cancela o usuário com o {user_id} correspondente

Candidates:
* GET /candidates                   -> Retorna todos os candidatos (não cancelados)
* GET /candidates/{candidate_id}    -> Retorna o candidato com {candidate_id} correspondente
* POST /candidates                  -> Cria um novo candidato
* PATCH /candidates/{candidate_id}  -> Edita um ou mais campos do candidato com {candidate_id} correspondente
* DELETE /candidates/{candidate_id} -> Cancela o candidato com {candidate_id} correspondente

Elections:
* GET /elections               -> Retorna todas as eleições
* GET /elections/{election_id} -> Retorna a eleição com o {election_id} correspondente
* POST /elections              -> Cria uma nova eleição

Votes:
* GET  /votes                -> Retorna todos os votos
* GET  /votes/{vote_id}      -> Retorna o voto com {vote_id} correspondente
* GET  /votes/{user_id}      -> Retorna todos os votos com {user_id} correspondentes
* GET  /votes/{candidate_id} -> Retorna todos os votos com {candidate_id} correspondentes
* GET  /votes/{election_id}  -> Retorna todos os votos com {election_id} correspondentes
* POST /votes                -> Cria um novo voto
