package transporter.data.sql.daoService.frontend.jinbag.services;

import transporter.data.sql.model.frontend.jinbag.entities.SemiProduct;

import java.util.List;

public interface ISemiProductService {
    List<SemiProduct> queryById(Long id);
}
