package br.com.gestao.igreja.endpoint;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.com.gestao.igreja.interfaces.repository.IPessoaRepository;

@RestController
@RequestMapping("/cadastro")
public class CadastroEndpoint {

    private  IPessoaRepository pessoaRepo;

    @Autowired
    public CadastroEndpoint(IPessoaRepository pessoaRepo){
        this.pessoaRepo = pessoaRepo;
    }
    @PostMapping("/pessoa")
    public ResponseEntity<?> cadastro(){
        return ResponseEntity.ok("Olá mundo");
    }
}
