package br.com.gestao.igreja.interfaces.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import br.com.gestao.igreja.model.Pessoa;

public interface IPessoaRepository extends JpaRepository<Pessoa, Long>{
    
}
