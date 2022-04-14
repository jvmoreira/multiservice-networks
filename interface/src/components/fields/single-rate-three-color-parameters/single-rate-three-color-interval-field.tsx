import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { SingleRateThreeColorParameterFieldProps } from './single-rate-three-color-parameters';

export function SingleRateThreeColorIntervalField(props: SingleRateThreeColorParameterFieldProps): ReactElement {
  const { singleRateThreeColorParameters, setSingleRateThreeColorParameters } = props;

  const singleRateThreeColorInterval = useMemo(() => {
    return singleRateThreeColorParameters.interval || '';
  }, [singleRateThreeColorParameters]);

  const setSingleRateThreeColorInterval = useSetNfvTeFunctionParameter('interval', setSingleRateThreeColorParameters);
  const onSingleRateThreeColorIntervalChangeHandler = useChangeHandler(setSingleRateThreeColorInterval);

  return (
    <FormInput
      label="Intervalo"
      name="interval"
      value={singleRateThreeColorInterval}
      placeholder="Valor em segundos"
      onChange={onSingleRateThreeColorIntervalChangeHandler}
    />
  );
}
