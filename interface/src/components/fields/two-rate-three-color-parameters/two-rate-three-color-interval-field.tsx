import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TwoRateThreeColorParameterFieldProps } from './two-rate-three-color-parameters';

export function TwoRateThreeColorIntervalField(props: TwoRateThreeColorParameterFieldProps): ReactElement {
  const { twoRateThreeColorParameters, setTwoRateThreeColorParameters } = props;

  const twoRateThreeColorInterval = useMemo(() => {
    return twoRateThreeColorParameters.interval || '';
  }, [twoRateThreeColorParameters]);

  const setTwoRateThreeColorInterval = useSetNfvTeFunctionParameter('interval', setTwoRateThreeColorParameters);
  const onTwoRateThreeColorIntervalChangeHandler = useChangeHandler(setTwoRateThreeColorInterval);

  return (
    <FormInput
      label="Intervalo"
      name="interval"
      value={twoRateThreeColorInterval}
      placeholder="Valor em segundos"
      onChange={onTwoRateThreeColorIntervalChangeHandler}
    />
  );
}
