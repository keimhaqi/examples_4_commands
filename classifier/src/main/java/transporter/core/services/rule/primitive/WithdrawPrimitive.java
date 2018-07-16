package transporter.core.services.rule.primitive;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import transporter.core.model.rule.IRule;
import org.springframework.context.annotation.Configuration;

import java.util.List;
import java.util.Map;

@Configuration
public class WithdrawPrimitive implements IRulePrimitive {
    private static Logger logger = LoggerFactory.getLogger(WithdrawPrimitive.class);

    private List<IRule> withdrawRules;

    @Override
    public boolean action(Map<String, Object> obj) {
        // do withdraw
        System.out.println("Do Withdraw");
        return false;
    }

    @Override
    public boolean action(String obj) {
        System.out.println("Withdraw " + obj);
        return false;
    }
}
