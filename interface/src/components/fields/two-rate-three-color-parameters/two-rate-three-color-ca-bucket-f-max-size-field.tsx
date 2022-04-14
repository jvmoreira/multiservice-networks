import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TwoRateThreeColorParameterFieldProps } from './two-rate-three-color-parameters';

export function TwoRateThreeColorCaBucketFMaxSizeField(props: TwoRateThreeColorParameterFieldProps): ReactElement {
  const { twoRateThreeColorParameters, setTwoRateThreeColorParameters } = props;

  const twoRateThreeColorCaBucketFMaxSize = useMemo(() => {
    return twoRateThreeColorParameters.ca_bucketF_max_size || '';
  }, [twoRateThreeColorParameters]);

  const setTwoRateThreeColorCaBucketFMaxSize = useSetNfvTeFunctionParameter('ca_bucketF_max_size', setTwoRateThreeColorParameters);
  const onTwoRateThreeColorCaBucketFMaxSizeChangeHandler = useChangeHandler(setTwoRateThreeColorCaBucketFMaxSize);

  return (
    <FormInput
      label="Tamanho Máximo do Bucket C do Color Aware"
      name="ca-bucket-f-max-size"
      value={twoRateThreeColorCaBucketFMaxSize}
      placeholder="Valor em tokens"
      onChange={onTwoRateThreeColorCaBucketFMaxSizeChangeHandler}
    />
  );
}
